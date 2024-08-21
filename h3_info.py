# ===========================================================================
# Python3 script
# ===========================================================================
import os
import sys
import getopt
import traceback
import h3

# ===========================================================================
# ===========================================================================
gVerbose = False
gMep1002Id = None

# ===========================================================================
# ===========================================================================


def showUsage():
    # type: () -> None
    script_name = os.path.basename(sys.argv[0])
    print(f"Usage: {script_name} [OPTIONS]")
    print("      -h, --help                 Show this help.")
    print("      -v, --verbose              Verbose output.")
    print(" ")


def getCommandLineArg():
    # type: () -> bool
    global gVerbose
    global gMep1002Id

    try:
        opts, arg_list = getopt.getopt(sys.argv[1:], "hv", [
            "help", "verbose", "url"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        showUsage()
        return False

    for o, a in opts:
        if o in ("-v", "--verbose"):
            gVerbose = True
        elif o in ("-u", "--url"):
            gStatBaseUrl = a
        elif o in ("-h", "--help"):
            showUsage()
            sys.exit()
        else:
            print("unhandled option")
            return False

    if len(arg_list) == 0:
        print("Missing ID.")
        return False
    gMep1002Id = arg_list[0]

    if gMep1002Id.startswith("0x"):
        gMep1002Id = gMep1002Id[2:]

    return True


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    # type: () -> None
    if (getCommandLineArg() == False):
        sys.exit(2)

    try:
        h3Index = hex(int(gMep1002Id))

        print(f"MEP1002 ID: {gMep1002Id} => h3Index=0x{h3Index}")

        if h3.h3_is_valid(h3Index):
            print("h3Index is valid.")
            geo_info = h3.h3_to_geo(h3Index)
            print(f"Centre point: {geo_info}")

    except Exception as e:
        print(str(e))
        # print(traceback.format_exc())
        sys.exit(2)


# ===========================================================================
# ===========================================================================
if __name__ == "__main__":
    main()
