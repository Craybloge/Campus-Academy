/* npm test exercices/2-valeur-et-reference.js

Instructions :
- lancez le test via la commande ci-dessus. Cela va échouer.
- ne changez rien du code, *excepté* le 1er paramètre de chaque `assert.strictEqual` pour faire passer le test
*/
import test from 'ava';
import { strict as assert } from 'assert';

test('valeur-et-reference', t => {
	let x = 'bonjour'
	let y = x

	y = 'au revoir'
	assert.strictEqual(x === 'bonjour', true)

	x = 'salut'
	assert.strictEqual(y === 'au revoir', true)

	const chienMignon = {
		mignon: true,
		age: 4,
		talents: ['toujours heureux', 'propre', 'aime la baballe']
	}
	const ageDuChien = chienMignon.age
	const autreChien = chienMignon
	const autreChienEstMignon = autreChien.mignon
	const talentsDuChienMignon = chienMignon.talents

	autreChien.mignon = false
	autreChien.age = 12

	chienMignon.age = 5
	talentsDuChienMignon.push('vraiment mignon')

	// remplacez les "???" par la bonne valeur
	// ps : on essaie de deviner dans sa tête, on affiche pas les variables dans la console ;)
	assert.strictEqual(ageDuChien == '4', true)
	assert.strictEqual(chienMignon.age == '5', true)
	assert.strictEqual(autreChien.age == '5', true)

	assert.strictEqual(autreChienEstMignon == true, true)
	assert.strictEqual(autreChien.mignon == false, true)
	assert.strictEqual(chienMignon.mignon == false, true)

	assert.strictEqual(chienMignon.talents.length == '4', true)
	assert.strictEqual(autreChien.talents.length == '4', true)
	assert.strictEqual(talentsDuChienMignon.length == '4', true)
});
