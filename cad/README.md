# cad/

Put your own design files here as the build progresses. Suggested layout:

```
cad/
  frame/        native CAD (Onshape export, Fusion .f3d, FreeCAD .FCStd) + STEP
  brackets/     DXF per part, named part_rNN.dxf, one revision per file
  drawings/     PDF drawings that went out for quotes
  cut-list.md   tube lengths/angles as sent to the tube cutter
```

Commit the exported STEP/DXF/PDF alongside native files so anyone (including you in
two years) can open them without the original software. See
`../07-cad-and-drawings/README.md` for export settings and
`../templates/drawing_checklist.md` before sending files out.
