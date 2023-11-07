(TeX-add-style-hook
 "lab"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "10pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("xcolor" "usenames" "dvipsnames" "svgnames" "table")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "amssymb"
    "amsmath"
    "graphicx"
    "mathtools"
    "xcolor"
    "multirow"
    "vmargin")
   (TeX-add-symbols
    "RR"
    "NN"
    "ZZ"
    "calP"
    "bfa"
    "bfb"
    "bfc"
    "bfd"
    "bfv"
    "bfw"
    "bfi"
    "bfj"
    "bfk"
    "sep"))
 :latex)

