from fovea import fovea_ext

# If this runs without crashing, your new C++ code is active!
test_link = fovea_ext.format_bionic_text("https://github.com", 0.5, ">>", "<<")

print("Output should just be the plain link (no >> or <<):")
print(test_link)