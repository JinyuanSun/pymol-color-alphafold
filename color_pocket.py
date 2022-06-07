from pymol import cmd


def coloraf(selection="all"):

    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Colors Alphafold structures by pLDDT

    USAGE
    coloraf sele

    PARAMETERS

    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """
    cmd.set_color("high_lddt_c", [0,0.325490196078431,0.843137254901961 ])
    cmd.set_color("normal_lddt_c", [0.341176470588235,0.792156862745098,0.976470588235294])
    cmd.set_color("medium_lddt_c", [1,0.858823529411765,0.070588235294118])
    cmd.set_color("low_lddt_c", [1,0.494117647058824,0.270588235294118])
    cmd.color("high_lddt_c", f"({selection}) and b > 0.9")
    cmd.color("normal_lddt_c", f"({selection}) and b < 0.90 and b > 0.70")
    cmd.color("medium_lddt_c", f"({selection}) and b < 0.70 and b > 0.50")
    cmd.color("low_lddt_c", f"({selection}) and b < 0.50")


cmd.extend("coloraf", coloraf)
cmd.auto_arg[0]["coloraf"] = [cmd.object_sc, "object", ""]
