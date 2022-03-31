import os
import sys
import time

with open(sys.argv[1], "r") as f:
    file = f.read()
    file = file.split("\n")

tokens = []

for line in file:
    token = line.split()

    tokens.append(token)

with open("output.py", "w") as f:
    f.write("") ## clear the output file
    # although im sure that there is a better way

start_indenting = False
writer = ""

variables = {}

with open("output.py", "a+") as f:
    writer += "import os\nimport time\n\n"
    for i in tokens:
        if len(i) > 0:

            #############
            #  COMMENT  #
            #############


            if i[0][:2] == "//":
                writer += F"## {i[1:]}\n"
                continue

            ################
            #  END INDENT  #
            ################

            if i[0][0] == "}":
                start_indenting = False ## stop indenting (for python)
                writer += "\n"
                continue

            ############
            #  INDENT  #
            ############

            if start_indenting == True:
                writer += "\t"

            ##################
            #  START INDENT  #
            ##################

            if i[-1] == "{":
                start_indenting = True
                i = i[:-1] ## remove left bracket

            ###########
            #  PRINT  #
            ###########

            if i[0] == "show":
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


                    shown = ''.join(final_statement)

                else:
                    shown = ''.join(i[1:])

                writer += f"print({shown})\n"
                continue

            ##############
            #  Variables #
            ##############

            if i[0] == "var":
                if i[3] == "true" or i[3] == "false":
                    if i[3] == "true":
                        statement = bool(1)
                    if i[3] == "false":
                        statement = bool(0)

                    print(temp_statement)
                else:
                    i = [j for j in i]
                    statement = " ".join(i[3:])

                try:
                    statement = int(statement)
                except:
                    statement = f"{statement}"

                if statement == "true":
                    statement = bool(1)
                if statement == "false":
                    statement = bool(0)

                variables[i[1]] = statement
                writer += f"{i[1]} = {statement}\n"
                continue

            ###############
            #  Functions  #
            ###############

            if i[0] == "|":
                parameters = ", ".join(i[3:])
                writer += f"def {i[1]}({parameters}):\n"
                continue

            ################
            #  While Loop  #
            ################

            if i[0] == "while": ## 1 > 0 {
                condition = i[1:]
                start_indenting = True

                final_condition = "".join(str(elm) for elm in condition)
                writer += f"while {str(final_condition)}:\n"
                continue

            ##############
            #  For Loop  #
            ##############

            if i[0] == "for": ## 1 > 0 {
                start_indenting = True
                writer += f"for {i[1]} in {i[3]}:\n"
                continue

            ###################
            #  Call function  #
            ##################

            if i[0] == ">":
                call_parameters = ", ".join(i[2:])
                writer += f"{i[1]}({call_parameters})\n"
                continue

            ########################
            #  In-built functions  #
            ########################

            if i[0] == ">>":
                if i[1] == "clear":
                    writer += "os.system('cls')\n"
                    continue

                if i[1] == "wait":
                    sleep_time = int(i[2])
                    writer += f"time.sleep({sleep_time})\n"
                    continue

            ##################
            #  if statement  #
            ##################

            if i[0] == "?":
                condition = i[1:]
                final_condition = "".join(str(elm) for elm in condition)
                writer += f"if {str(final_condition)}:\n"
                continue

            ################
            #  INC BY ONE  #
            ################

            if i[0] == "++":
                writer += f"{i[1]} += 2\n"

            #################
            #  ADD MODULES  #
            #################

            if i[0] == "add":
                writer += f"import {i[1]}\n\n"

    f.write(writer)

os.system("py output.py")
