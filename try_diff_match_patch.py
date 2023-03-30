from diff_match_patch import diff_match_patch

dmp = diff_match_patch()

diff = dmp.diff_main("hello world.", "goodbye world!")
# print(f"{diff=}")
dmp.diff_cleanupSemantic(diff)
print(f"{diff=}")

err = """also, you'll meet friendly people who usually ask to you something to be friends and change your telephone number."""
correct = """also, you'll meet friendly people who usually ask you to be friends and exchange telephone numbers."""
diff = dmp.diff_main(err, correct)
# print(f"{diff=}")
dmp.diff_cleanupSemantic(diff)
print(f"{diff=}")

err = """volleyball is a sport play every place, when i travel on the beach i like plays with my sister in the sand and after we are going to the sea."""
correct = """volleyball is a sport that is played everywhere. when i am on the beach i like playing with my sister in the sand and then we go in the sea."""
diff = dmp.diff_main(err, correct)
# print(f"{diff=}")
dmp.diff_cleanupSemantic(diff)
print(f"{diff=}")