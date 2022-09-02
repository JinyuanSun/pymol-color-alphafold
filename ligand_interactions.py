import pymol

def ligand_interactions(selection="all"):

    """
    AUTHOR
    Jinyuan Sun
    DESCRIPTION
    Show interactions between ligands and receptor
    USAGE
    ligand_interactions sele
    PARAMETERS
    sele (string)
    The name of the selection/object to show interactions between ligands and receptor. Default: all
    """
    pymol.cmd.set('valence',0)
    pymol.cmd.h_add('polymer.protein AND (element O,N,S)')
    pymol.preset.ligands()
    pymol.cmd.select('pocket','br. all within 5 of organic')
    pymol.cmd.set('line_as_cylinders')
    pymol.cmd.label('pocket and name CA','"%s%s" % (resi, resn)')
    pymol.cmd.set('float_labels')
    pymol.cmd.color('wheat','polymer.protein and ele C')
    pymol.cmd.color('white','organic and ele C')
    pymol.cmd.hide('ribbon')
    pymol.cmd.show('cartoon')
    pymol.cmd.set('line_radius', 0.2)
    pymol.cmd.hide('(ele h and not neighbor (ele n+o+s))')
    pymol.cmd.zoom('pocket')
    pymol.cmd.show('surface', 'polymer.protein')
    pymol.cmd.set('surface_color', 'white', '*')
    pymol.cmd.set('transparency', 0.7)
    pymol.cmd.set('stick_h_scale', 1)
    pymol.cmd.hide('line','polymer.protein and (name c,n,o)')
    pymol.cmd.set('cartoon_side_chain_helper')

pymol.cmd.extend("ligand_interactions", ligand_interactions)
pymol.cmd.auto_arg[0]["ligand_interactions"] = [pymol.cmd.object_sc, "object", ""]
