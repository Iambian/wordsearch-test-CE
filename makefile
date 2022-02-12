# ----------------------------
# Makefile Options
# ----------------------------

NAME = WSEARCH
ICON = icon.png
DESCRIPTION = "Demonstration Word Searcher"
COMPRESSED = NO
ARCHIVED = NO

CFLAGS = -Wall -Wextra -Oz
CXXFLAGS = -Wall -Wextra -Oz

# ----------------------------

include $(shell cedev-config --makefile)
