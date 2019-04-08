from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="mpusz", login_username="mpusz",
                                 channel="testing",
                                 upload="https://api.bintray.com/conan/mpusz/conan-mpusz")
    builder.add_common_builds(pure_c=False)
    builder.run()
