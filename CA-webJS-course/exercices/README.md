## Installation

1. Node.js doit être installé. Si vous ne l'avez pas déjà :
- sur votre mac, installez-le via Homebrew : `brew install node` (pour installer Homebrew si vous ne l'avez pas : https://brew.sh/index_fr)
- sur Windows, installez-le via Chocolatey : `choco install -y nodejs` (pour installer Chocolatey si vous ne l'avez pas : https://chocolatey.org/install#individual)
- sur Linux via le gestionnaire de paquets de votre système : https://nodejs.org/en/download/package-manager/

2. Installer les dépendances de ce projet:

```
cd exercices-rappel-js/
npm install
```

3. Vérifier que l'installation est OK en lançant:

```
npm test check-install.js
```

## Pour faire un exercice

Chaque exercice est en réalité un fichier à lancer via "npm test" pour valider que l'exercice est réussi ou non.

Dans votre terminal, restez dans le dossier "exercices-rappel-js" et lancez au cas par cas chaque exercice. Exemple :

```
npm test exercices/1-let-et-const.js
```

Si le test retourne un texte vert qui dit que "ça passe", c'est OK ! L'exercice est réussi. 

Chaque exercice a la consigne décrite en haut du fichier.
