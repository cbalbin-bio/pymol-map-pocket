from pymol import cmd, stored


def pock2prot(pocket, protein):

    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Maps atoms that are part of a pocket to the full protein

    USAGE
    pock2prot pocket, protein

    PARAMETERS

    pocket (string)
    The name of the selection/object representing the pocket

    protein (string)
    The name of the selection/object representing protein of which the pocket is a member of
    """

    cmd.select(pocket)
    stored.serial_nums = []
    cmd.iterate("sele", "stored.serial_nums.append(ID)")

    selection = []
    for serial_num in stored.serial_nums:
        selection.append(f"id {serial_num} ")

    selection = f"m. {protein} and " + "+ ".join(selection)
    cmd.select(f"{protein}_{pocket}", selection)


cmd.extend("pock2prot", pock2prot)
cmd.auto_arg[0]["pock2prot"] = [cmd.object_sc, "object", ""]
cmd.auto_arg[1]["pock2prot"] = [cmd.object_sc, "object", ""]
