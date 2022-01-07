/* npm test exercices/5-la-totale.js

Instructions :
- Implémentez les différentes fonctions vides pour que les tests passent
- ne changez pas les lignes `assert...`
*/
import test from 'ava';
import { strict as assert } from 'assert';

// ne pas modifier directement cette constante
const Actors = [
	{ name: 'Winslet', firstname: 'Kate', gender: 'F', height: 169, hasOscars: true },
	{ name: 'Johansson', firstname: 'Scarlett', gender: 'F', height: 163, hasOscars: false },
	{ name: 'Carrey', firstname: 'Jim', gender: 'M', height: 190, hasOscars: true },
	{ name: 'Ruffalo', firstname: 'Mark', gender: 'M', height: 175, hasOscars: false },
	{ name: 'Dunst', firstname: 'Kirsten', gender: 'F', height: 171, hasOscars: true }
]

// implémentez cette fonction, qui prend en paramètre un tableau d'actrices et acteurs, et qui retourne les actrices ayant un oscar
const filterActressesWithOscars = actors => {
	return actors.filter(({gender, hasOscars}) => gender == "F" && hasOscars)
}

// implémentez cette fonction, qui prend en paramètre un tableau d'actrices et acteurs, et qui retourne un tableau contenant les mêmes actrices et acteurs, tous ayant un nouvelle propriété "fans" avec pour valeur `1`
// ! attention ! on ne veut pas modifier les objets d'origines du `actors` passé (si c'est le cas, les tests échouent)
const addFans = actors => {
	return actors.map(actor => ({
			...actor,
			fans: 1	
		}))
}

// implémentez cette fonction, qui prend en paramètre un tableau d'actrices/acteurs, et retourne un tableau de ces actrices/acteurs sans l'info du genre
// utilisez l'opérateur rest
// ! attention ! on ne veut pas modifier les objets d'origines du `actors` passé (si c'est le cas, les tests échouent)
const withoutGenderInfo = actors => {
	return actors.map(actor => {
		const {gender, ...rest} = actor
		return rest	
	})
}

// implémentez cette fonction qui retourne le nom complet d'un acteur
// consigne : ne pas utiliser l'opérateur "+"
const getFullName = (actor) => {
		const {firstname, name} = actor
		return `${firstname} ${name}`


}

// implémentez cette fonction qui prend un tableau d'acteurs/actrices en paramètre
// et qui retourne ces acteurs/actrices sans leur "name" ni "firstname", mais avec une nouvelle propriété "fullname" qui utilise `getFullName()`
// ! attention ! on ne veut pas modifier les objets d'origines du `actors` passé (si c'est le cas, les tests échouent)
const getRenamedActors = actors => {
	return actors.map(actor => {
		const {firstname, name, ...rest} = actor
		rest.fullname = getFullName(actor)
		return rest	
	})

}

console.log(addFans(Actors));


test('la-totale', () => {
	assert.deepStrictEqual(
		filterActressesWithOscars(Actors),
		[Actors[0], Actors[4]]
	)
	assert.strictEqual(
		filterActressesWithOscars(Actors)[0],
		Actors[0]
	)

	assert.strictEqual(typeof addFans(Actors)[0].fans !== "undefined", true)
	assert.strictEqual(typeof addFans(Actors)[1].fans !== "undefined", true)
	assert.strictEqual(typeof addFans(filterActressesWithOscars(Actors))[1].fans !== "undefined", true)
	assert.notStrictEqual(addFans(Actors)[0], Actors[0])

	assert.strictEqual(typeof Actors[0].gender === "undefined", false)
	assert.strictEqual(typeof withoutGenderInfo(Actors)[0].gender === "undefined", true)

	assert.strictEqual(getFullName(Actors[3]), 'Mark Ruffalo')
	assert.strictEqual(typeof Actors[0].fullname === "undefined", true)
	assert.strictEqual(getRenamedActors(Actors)[0].fullname === "Kate Winslet", true)
})
