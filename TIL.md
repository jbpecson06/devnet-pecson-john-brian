# TIL — Today I Learned

A running log of small things you learn along the way — not a full topic,
just quick notes whenever something clicks or trips you up. Add to this
anytime, not just during formal lessons.

## Example (delete this once you add your own)
- Found out that shutil.move() will silently overwrite a file at the destination if it already exists there with the same name.

- Found two ways to get the extension of a file: os.path.splitext(filename) (returns a tuple e.g. ("report", ".pdf")) or a simpler filename.split(".")[-1] Both will work fine for a simple sorting script.