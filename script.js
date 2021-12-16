const tasks = [
    'Révisions',
    'JS sans framework',
    'React'
]
let compteur = 0
tasks.forEach(element => {
	compteur++
    addTask(element, compteur)
})

document.querySelector("#addTask").onclick = () => {
	compteur++
    addTask(document.querySelector('#name').value, compteur)
}
function addTask(input, compteur) {
    const line = document.createElement('li');
    line.setAttribute("id", "tache" + compteur)

    const checkbox = document.createElement('input')
    checkbox.setAttribute("type", "checkbox")
    checkbox.setAttribute("id", "tache" + compteur + "-checkbox")

    const label = document.createElement('label')
    label.setAttribute("for", "tache" + compteur + "-checkbox")
    label.setAttribute("id", "tache" + compteur + "-label")
    label.textContent = input +" "

    const button = document.createElement('button')
    button.setAttribute("type", "button")
    button.textContent = "Supprimer"
    button.onclick = () => {
        line.remove()
    }

    document.querySelector('#taskList').appendChild(line)
    document.querySelector("#tache" + compteur).appendChild(checkbox)
    document.querySelector("#tache" + compteur).appendChild(label)
    document.querySelector("#tache" + compteur).appendChild(button)
  }

  function checked(id, input) {
	  document.querySelector("#" + id)
  }