import sys
import os

def traite(nom_fich):
    if not os.path.exists(nom_fich):
        print(f"Le fichier {nom_fich} n'existe pas")
    else:
        f = open(nom_fich, "r", encoding="utf-8")
        txt = f.read()
        f.close()

        nouveau_txt = ""

        i = txt.find("```sql")
        while i != -1:
            ni = txt.find("```sql", i+1)
            ii = txt.find("```\n", i)
            if ii < ni:
                nouveau_txt+=txt[i+len("```sql"):ii]+"\n"
            i = ni


        nouveau_nom_fich = ".".join(nom_fich.split(".")[:-1])+".sql"

        print(nouveau_nom_fich)

        nf = open(nouveau_nom_fich, "w", encoding="utf-8")
        nf.write(nouveau_txt)
        nf.close()

def main():
    for x in range(1, len(sys.argv)):
        traite(sys.argv[x])


if __name__ == "__main__":
    main()
