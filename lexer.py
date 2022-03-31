import os
import time

with open("test.al", "r") as f:
    file = f.read()
    file = file.split("\n")

tokens = []

for line in file:
    token = line.split()

    tokens.append(token)

with open("output.py", "w") as f:
    f.write("") ## clear the output file
    # although im sure that there is a better way


with open("output.py", "a+") as f:
    f.write("import os\n\n")
    for i in tokens:
        if len(i) > 0:
            if i[0] == "#":
                print(i, "   COMMENT")
                continue

            ###########
            #  PRINT  #
            ###########

            if i[0] == "show":
                print(i, "   SHOW")
                stm = i[1:]
                if len(stm) > 1:
                    #shown = []#','.join(i[1:])
                    final_statement = []
                    temp_statement = []
                    string_start = False
                    for index, elm in enumerate(stm):
                        try:
                            if stm[index + 1][0] == "'" or stm[index + 1][0] == '"':
                                temp_statement.append(elm)
                                temp_statement.append(",")
                                string_start = True

                            elif stm[index][-1] == "'" or stm[index][-1] == '"':
                                temp_statement.append(elm)
                                final_statement.append(" ".join(temp_statement))
                                temp_statement = []
                                final_statement.append(",")
                                string_start = False

                            elif string_start == True:
                                temp_statement.append(elm)

                            else:
                                final_statement.append(elm)

                        except:
                            final_statement.append(elm)


                    print(final_statement)
                    shown = ''.join(final_statement)

                else:
                    shown = ''.join(i[1:])
                    shown = ''.join(final_statement)

                f.write(f"print({shown})\n")
                continue

            ##############
            #  Variables #
            ##############

            if i[0] == "var":
                print(i, "   VAR")
                statement = eval("".join(i[3:]))
                try:
                    statement = int(statement)
                except:
                    statement = f"'{statement}'"

                f.write(f"{i[1]} = {statement}\n")
                continue

            ###############
            #  Functions  #
            ###############

            if i[0] == "|":
                print(i, "   FUNC")
                f.write(f"def {i[1]}():\n\t")
                continue

            if i[0] == "while":
                print(i, "   WHILE")
                condition = i[1:]
                final_condition = "".join(str(elm) for elm in condition)
                f.write(f"while {str(final_condition)}:\n\t")
                continue

            ###################
            #  Call function  #
            ##################

            if i[0] == ">":
                print(i, "   CALL FUNC")
                f.write(f"{i[1]}()\n")
                continue

            ########################
            #  In-built functions  #
            ########################

            if i[0] == ">>":
                if i[1] == "clear":
                    f.write("os.system('clear')\n")
                    continue

            ##################
            #  if statement  #
            ##################

            if i[0] == "?":
                condition = i[1:]
                final_condition = "".join(str(elm) for elm in condition)
                f.write(f"if {str(final_condition)}:\n\t")
                continue
