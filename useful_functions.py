import sys
def treat_user_input(user_input):
    try:
        if "," in user_input:
            user_input = user_input.split(",")
            for i in range(len(user_input)):
                user_input[i] = user_input[i].strip()
                user_input[i] = int(user_input[i])
        else:
            user_input = int(user_input)
    except TypeError as error:
        print("Você não digitou uma entrada válida! Insira apenas o número dos indices. Erro:\n", error.__class__, f"-> {error.name}")
        sys.exit()
    return user_input