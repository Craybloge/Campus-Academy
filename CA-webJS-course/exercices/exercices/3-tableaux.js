/* npm test exercices/3-tableaux.js

Instructions :
- Implémentez la fonction "concatStringArray" comme vous voulez pour que le 1er test passe
- Implémentez la fonction "removeEmptyLines" avec une seule expression pour que le 2e test passe
- ne changez pas les lignes `assert...`
*/

import test from 'ava';
import { strict as assert } from 'assert';
assert.strictEqual(true, true)

function concatStringArray(stringArray) {
	return stringArray.join('');
	// let element = "";
	// for (let index = 0; index < stringArray.length; index++) {
	// 	element += stringArray[index];
	// }
	// return element
}

test('concatStringArray', t => {
	assert.strictEqual(concatStringArray([]), '');
	assert.strictEqual(concatStringArray(['abc']), 'abc');
	assert.strictEqual(concatStringArray(['x', 'y', 'z']), 'xyz');
});

const removeEmptyLines = (lines) => {
	// consigne: n'utilisez qu'une seule ligne de code dans cette fonction
	return lines.join('').split(''); 
}

const plusOne = (numbers) => {
	// consigne: n'utilisez qu'une seule ligne de code dans cette fonction
	return numbers.map(x => x + 1);
}

test('removeEmptyLines()', () => {
	assert.deepStrictEqual(
		removeEmptyLines(['', 'a', 'b', '', '', 'c', 'd', '']),
		['a', 'b', 'c', 'd']
	);
	assert.deepStrictEqual(
		removeEmptyLines([]),
		[]
	);
	assert.deepStrictEqual(
		removeEmptyLines(['a']),
		['a']
	);
	assert.deepStrictEqual(
		removeEmptyLines(['a', 'b']),
		['a', 'b']
	);
	assert.deepStrictEqual(
		removeEmptyLines(['']),
		[]
	);
	assert.deepStrictEqual(
		removeEmptyLines(['', 'a', '']),
		['a']
	);
});

test('plusOne', () => {
	assert.deepStrictEqual(
		plusOne([1, 2, 3, 4]),
		[2, 3, 4, 5]
	);
	assert.deepStrictEqual(
		plusOne([12, 22, 33, 44]),
		[13, 23, 34, 45]
	);
	assert.deepStrictEqual(
		plusOne([]),
		[]
	);
})
