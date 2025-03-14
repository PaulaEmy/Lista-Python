texto = '''The Python Software Foundation and the global Python
community welcome and encou
rage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''
texto = texto.lower()
texto = texto.replace(',', ' ')
texto = texto.replace('.', ' ')
texto = texto.replace(':', ' ')

texto = texto.split()
for p in texto:
    if p[0] in 'python' or p[-1] in 'python':
        print(p)
