// user.test.js
import { createUser } from './User';

test('should create a user object', () => {
  const user = createUser('John', 30);
  expect(user).toEqual({ name: 'John', age: 30 });
});
