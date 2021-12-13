#!/usr/bin/env python3
from os import walk, path

DriveMountLetters = ['U:/', 'V:/', 'W:/', 'X:/', 'Y:/', 'Z:/']


def get_all_folders_and_files(Drives):
    WorkingTempVar = []

    for Drive in Drives:
        for (DirPath, DirNames, FileNames) in walk(path.normpath(Drive)):
            WorkingTempVar.append([DirPath, FileNames])

    return WorkingTempVar


def find_identifier_files(Directory):
    pass


if __name__ == '__main__':
    for x in get_all_folders_and_files(DriveMountLetters):
        print(x)
