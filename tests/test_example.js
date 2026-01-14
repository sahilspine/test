const assert = require('assert');

describe('Basic Tests', () => {
  it('should pass simple addition', () => {
    assert.strictEqual(2 + 2, 4);
  });

  it('should handle strings', () => {
    assert.strictEqual('hello', 'hello');
  });

  it('should work with arrays', () => {
    const arr = [1, 2, 3];
    assert.strictEqual(arr.length, 3);
  });
});
