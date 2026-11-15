# Tuwaiq Club Certificates

Certificate of Appreciation generator for Tuwaiq Club (supported by Tuwaiq Academy | PNU). The presenter answers a few questions in a terminal (name, program, dates, training hours) and their certificate builds itself with animation. The finished certificate downloads as an A4 PDF.

- The design comes from the club's Canva certificate.
- Names are never stored or sent anywhere; everything runs in the visitor's browser.

## Editing

- **Programs list:** edit `PROGRAMS` near the top of the script in `src/template.html`. Picking a listed program fills its dates; any other program asks for the dates.
- **Rebuild:** run `python src/build.py`. It writes `index.html`, a single file with the fonts and images built in. Then commit and push.
- **Check the layout:** open `index.html?preview=1&name=Your%20Name` to jump straight to the finished certificate.

Credits: keyboard sounds from the CC0 "Keyboard Soundpack #1" by unicaegames (OpenGameArt). Fonts: Exo 2, IBM Plex Sans, JetBrains Mono (SIL Open Font License).
