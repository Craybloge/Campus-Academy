/* npm test exercices/1-let-et-const.js

Instructions :
- lancez le test via la commande ci-dessus. Cela va échouer.
- sans changer les lignes `assert.strictEqual`, corrigez le code existant ou rajoutez-en pour faire passer le test.
*/
import test from 'ava';
import { strict as assert } from 'assert';

test('let-et-const', t => {
	const x = 42; // ps : interdit de toucher à cette ligne 
	let y = 4;
	assert.strictEqual(x, 42);
	if (false) {
		assert.strictEqual(x, 40);
	}
	assert.strictEqual(x, 42);
	y = 12;
	assert.strictEqual(y, 12);
});
