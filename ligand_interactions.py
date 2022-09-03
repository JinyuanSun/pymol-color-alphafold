import pymol

def ligand_interactions(surface=True):

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
    pymol.cmd.select('pocket','br. all within 5 of organic')
    pymol.cmd.show('line','pocket and polymer.protein')
    pymol.cmd.show('sticks','organic')
    pymol.cmd.set('line_as_cylinders')
    pymol.cmd.label('pocket and name CA','"%s%s" % (resi, resn)')
    pymol.cmd.set('float_labels')
    pymol.cmd.color('wheat','polymer.protein and ele C')
    pymol.cmd.color('titanium','organic and ele C')
    pymol.cmd.hide('ribbon')
    pymol.cmd.show('cartoon')
    pymol.cmd.set('line_radius', 0.2)
    pymol.cmd.hide('(ele h and not neighbor (ele n+o+s))')
    pymol.cmd.zoom('pocket')
    if surface:
        pymol.cmd.show('surface', 'polymer.protein')
        pymol.cmd.set('surface_color', 'white', '*')
        pymol.cmd.set('transparency', 0.7)
    pymol.cmd.set('stick_h_scale', 1)
    pymol.cmd.hide('line','polymer.protein and (name c,n,o)')
    pymol.cmd.set('cartoon_side_chain_helper')
    pymol.cmd.distance("pi-interactions", 'organic', 'polymer.protein', 4, 5)
    pymol.cmd.color('bluewhite', 'pi-interactions')
    pymol.cmd.distance("h-bonds", 'organic', 'polymer.protein', 4, 2)


pymol.cmd.extend("ligand_interactions", ligand_interactions)
pymol.cmd.auto_arg[0]["ligand_interactions"] = [pymol.cmd.object_sc, "object", ""]
