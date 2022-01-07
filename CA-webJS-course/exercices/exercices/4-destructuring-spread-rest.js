/* npm test exercices/4-destructuring-spread-rest.js

Instructions :
- Changez le code pour utiliser du destructuring et des opérateurs "spread"/"rest" et faire que les tests passent
- ne changez pas les lignes `assert...`
*/
import test from 'ava';
import { strict as assert } from 'assert';

test('Destructuring', t => {
	const Guile = {
		firstname: 'Jean Claude',
		lastname: 'Van Damme',
	};

	const lostNumbers = [4, 8, 15, 16, 23, 42]
	
	// DÉBUT : utilisez du destructuring ici pour créer "firstname" et "lastname"
	const {firstname, lastname} = Guile;
	// FIN


	assert.strictEqual(firstname, 'Jean Claude');
	assert.strictEqual(lastname, 'Van Damme');

	// DÉBUT : utilisez du destructuring ici pour créer "firstNumber", "secondNumber", "otherNumbers"
	const [firstNumber, secondNumber, ...otherNumbers] = lostNumbers
	// FIN

	assert.strictEqual(firstNumber, 4);
	assert.strictEqual(secondNumber, 8);
	assert.deepStrictEqual(otherNumbers, [15, 16, 23, 42]);
});

test('Spread', t => {
	const chienMignon = {
		mignon: true,
		age: 4,
	}

	// DÉBUT : utilisez l'opérateur spread ici pour faire passer les tests
	const autreChien = {...chienMignon}
	// FIN

	assert.notStrictEqual(autreChien, chienMignon)

	const chienMignonEtTalentueux = {
		mignon: true,
		age: 5,
		talents: ['la baballe', 'les belly hugs']
	}

	// DÉBUT : utilisez l'opérateur spread ici pour faire passer les tests
	const autreChienTalentueux = {...chienMignonEtTalentueux, talents : [...chienMignonEtTalentueux.talents]}
	// FIN

	assert.notStrictEqual(autreChienTalentueux, chienMignonEtTalentueux)
	assert.notStrictEqual(autreChienTalentueux.talents, chienMignonEtTalentueux.talents)
	assert.strictEqual(autreChienTalentueux.mignon, true)
    assert.strictEqual(autreChienTalentueux.age ,5)
    assert.strictEqual(autreChienTalentueux.talents[0], 'la baballe')

})

test('Rest', t => {
	// implémentez cette fonction pour que les tests passent
	function bonjourAJeSaisPasCombienDeGens(...gens) {
		return gens.map(x => "Salut " + x + " !").join(' ')
	}

	assert.strictEqual(
		bonjourAJeSaisPasCombienDeGens('Jean'),
		'Salut Jean !'
	)

	assert.strictEqual(
		bonjourAJeSaisPasCombienDeGens('Jean', 'Claude'),
		'Salut Jean ! Salut Claude !'
	)

	assert.strictEqual(
		bonjourAJeSaisPasCombienDeGens('Jean', 'Claude', 'Pierre'),
		'Salut Jean ! Salut Claude ! Salut Pierre !'
		)
		console.log(bonjourAJeSaisPasCombienDeGens('Jean', 'Claude', 'Pierre'));

	assert.strictEqual(
		bonjourAJeSaisPasCombienDeGens('Marie', 'Jacques', 'Annelyse', 'Coline', 'François', 'Aurélie', 'Moundir', 'Martin'),
		'Salut Marie ! Salut Jacques ! Salut Annelyse ! Salut Coline ! Salut François ! Salut Aurélie ! Salut Moundir ! Salut Martin !'
	)
})