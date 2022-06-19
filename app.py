def combine_subtitle(subtitle1, subtitle2, output):
    with open(subtitle1, "r", encoding="utf-8") as f:
        sub1_txt = f.readlines()

    with open(subtitle2, "r", encoding="utf-8") as f:
        sub2_txt = f.readlines()


    sub1_join = "".join(sub1_txt)
    sub2_join = "".join(sub2_txt)


    sub1_each = sub1_join.split("\n\n")
    sub2_each = sub2_join.split("\n\n")

    combiner1 = [x + '\n\n' + y for x, y in zip(sub1_each, sub2_each)]

    combiner2 = "\n\n".join(combiner1)

    if output == "":
        with open("combined.srt", "w") as files:
            files.writelines(combiner2)
    else:
        with open(output, "w") as files:
            files.writelines(combiner2)
    print("Process Completed")


sub1 = input("Subtitle 1: ")
sub2 = input("Subtitle 2: ")
output = input("Output (Default: combined.srt): ")
combine_subtitle(sub1, sub2, output)