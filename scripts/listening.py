#!/usr/bin/env python3
"""Turn a listening script into an exam-style audio file with macOS voices.

Script format (one turn per line, blank lines and lines starting with # ignored):
    A: Hello, thanks for coming in today.
    B: It's a pleasure.
Lines without a "X:" prefix are read by the narrator (speaker N).

Usage:
    python3 scripts/listening.py listening/2026-10-02-interview.txt
    python3 scripts/listening.py FILE --twice --rate 160 --voices "A=Daniel,B=Moira"
    Voices: A/B British, C Irish, D Australian, N narrator (British, distinct from A).

Output: FILE with .m4a extension (copy it to the Pixel, or AirDrop/Drive).
"""
import argparse
import re
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

# Voices are chosen by base name + locale, because macOS shows voice names in the
# system language (e.g. "Flo (Inglés (RU))" on a Spanish Mac, "Flo (English (UK))"
# on an English one). Each speaker lists fallbacks in order of preference.
DEFAULT_VOICES = {
    "N": ["Reed@en_GB", "Eddy@en_GB", "Daniel@en_GB"],    # narrator, distinct from A
    "A": ["Daniel@en_GB"],
    "B": ["Flo@en_GB", "Shelley@en_GB", "Sandy@en_GB"],
    "C": ["Moira@en_IE"],
    "D": ["Karen@en_AU"],
}
VOICE_LINE = re.compile(r"^(.*?)\s+([a-z]{2,3}_[A-Z0-9]{2,3})\s+#")


def installed_voices():
    out = subprocess.run(["say", "-v", "?"], capture_output=True, text=True, check=True).stdout
    voices = []
    for line in out.splitlines():
        m = VOICE_LINE.match(line)
        if m:
            voices.append((m.group(1).strip(), m.group(2)))
    return voices


def resolve(spec, installed):
    """'Flo@en_GB' -> the installed full name, or None. 'Daniel' matches any locale."""
    base, _, locale = spec.partition("@")
    for name, loc in installed:
        if (name == base or name.startswith(base + " (")) and (not locale or loc == locale):
            return name
    return None


RATE = 22050
TURN = re.compile(r"^\s*([A-Z])\s*:\s*(.+)$")


def parse(path: Path):
    turns = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = TURN.match(line)
        turns.append((m.group(1), m.group(2)) if m else ("N", line))
    return turns


def synth(text: str, voice: str, wpm: int, out: Path):
    subprocess.run(
        ["say", "-v", voice, "-r", str(wpm), f"--data-format=LEI16@{RATE}", "-o", str(out), text],
        check=True,
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("script", type=Path)
    ap.add_argument("--rate", type=int, default=175, help="words per minute (default 175; try 150 to start)")
    ap.add_argument("--pause", type=float, default=0.6, help="seconds of silence between turns")
    ap.add_argument("--twice", action="store_true", help="play the whole recording twice, like Cambridge/IELTS")
    ap.add_argument("--voices", default="", help='override, e.g. "A=Daniel,B=Moira"')
    args = ap.parse_args()

    wanted = {k: list(v) for k, v in DEFAULT_VOICES.items()}
    for pair in filter(None, args.voices.split(",")):
        if "=" not in pair:
            sys.exit(f'Bad --voices entry "{pair}". Use SPEAKER=VOICE, e.g. "B=Moira" or "B=Flo@en_GB".')
        k, v = pair.split("=", 1)
        wanted[k.strip().upper()] = [v.strip()]

    installed = installed_voices()
    voices = {}
    for speaker, specs in wanted.items():
        name = next((n for n in (resolve(sp, installed) for sp in specs) if n), None)
        if not name:
            sys.exit(f"No installed voice for speaker {speaker} (tried {', '.join(specs)}). "
                     "Install one in System Settings > Accessibility > Spoken Content > System voice > Manage Voices, "
                     "or pick another with --voices. List voices with: say -v '?'")
        voices[speaker] = name

    turns = parse(args.script)
    if not turns:
        sys.exit("No text found in script.")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        frames = []
        silence = b"\x00\x00" * int(RATE * args.pause)
        for i, (speaker, text) in enumerate(turns):
            if speaker not in voices:
                sys.exit(f'Unknown speaker "{speaker}:" in script. Use A-D, or add it with --voices "{speaker}=VOICE".')
            voice = voices[speaker]
            part = tmp / f"{i:04d}.wav"
            synth(text, voice, args.rate, part)
            with wave.open(str(part)) as w:
                frames.append(w.readframes(w.getnframes()))
            frames.append(silence)
        audio = b"".join(frames)
        if args.twice:
            audio = audio + b"\x00\x00" * RATE * 3 + audio

        wav = tmp / "all.wav"
        with wave.open(str(wav), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(RATE)
            w.writeframes(audio)
        out = args.script.with_suffix(".m4a")
        subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", str(wav), str(out)], check=True)

    print(f"Wrote {out} ({len(audio) / 2 / RATE:.0f} s)")


if __name__ == "__main__":
    main()
