(TeX-add-style-hook
 "lab"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("tcolorbox" "breakable") ("fontenc" "T1") ("ucs" "mathletters") ("inputenc" "utf8x") ("adjustbox" "Export") ("enumitem" "inline") ("ulem" "normalem")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "tcolorbox"
    "parskip"
    "graphicx"
    "caption"
    "float"
    "xcolor"
    "enumerate"
    "geometry"
    "amsmath"
    "amssymb"
    "textcomp"
    "upquote"
    "eurosym"
    "iftex"
    "fontenc"
    "alphabeta"
    "ucs"
    "inputenc"
    "fontspec"
    "unicode-math"
    "fancyvrb"
    "grffile"
    "adjustbox"
    "hyperref"
    "titling"
    "longtable"
    "booktabs"
    "array"
    "calc"
    "enumitem"
    "ulem"
    "mathrsfs")
   (TeX-add-symbols
    '("Verbatim" ["argument"] 0)
    '("prompt" 4)
    '("WarningTok" 1)
    '("InformationTok" 1)
    '("AttributeTok" 1)
    '("PreprocessorTok" 1)
    '("ExtensionTok" 1)
    '("BuiltInTok" 1)
    '("OperatorTok" 1)
    '("ControlFlowTok" 1)
    '("VariableTok" 1)
    '("CommentVarTok" 1)
    '("AnnotationTok" 1)
    '("DocumentationTok" 1)
    '("ImportTok" 1)
    '("SpecialStringTok" 1)
    '("VerbatimStringTok" 1)
    '("SpecialCharTok" 1)
    '("ConstantTok" 1)
    '("NormalTok" 1)
    '("ErrorTok" 1)
    '("RegionMarkerTok" 1)
    '("FunctionTok" 1)
    '("AlertTok" 1)
    '("OtherTok" 1)
    '("CommentTok" 1)
    '("StringTok" 1)
    '("CharTok" 1)
    '("FloatTok" 1)
    '("BaseNTok" 1)
    '("DecValTok" 1)
    '("DataTypeTok" 1)
    '("KeywordTok" 1)
    "tightlist"
    "Wrappedvisiblespace"
    "Wrappedcontinuationsymbol"
    "Wrappedcontinuationindent"
    "Wrappedafterbreak"
    "Wrappedbreaksatspecials"
    "Wrappedbreaksatpunct"
    "boxspacing"
    "Oldincludegraphics"
    "br"
    "gt"
    "lt"
    "Oldtex"
    "Oldlatex"
    "PY"
    "PYZbs"
    "PYZus"
    "PYZob"
    "PYZcb"
    "PYZca"
    "PYZam"
    "PYZlt"
    "PYZgt"
    "PYZsh"
    "PYZpc"
    "PYZdl"
    "PYZhy"
    "PYZsq"
    "PYZdq"
    "PYZti"
    "PYZat"
    "PYZlb"
    "PYZrb"
    "PYGZus"
    "PYGZob"
    "PYGZcb"
    "PYGZca"
    "PYGZam"
    "PYGZlt"
    "PYGZgt"
    "PYGZsh"
    "PYGZpc"
    "PYGZdl"
    "PYGZhy"
    "PYGZsq"
    "PYGZdq"
    "PYGZti"
    "OriginalVerbatim"
    "FancyVerbFormatLine")
   (LaTeX-add-labels
    "lab-4-collisions"
    "abstract"
    "introduction"
    "experimental-procedure"
    "conclusion")
   (LaTeX-add-environments
    "Shaded"))
 :latex)

