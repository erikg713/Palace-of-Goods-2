describe('E2E Tests', () => {
  before(() => {
    // Use fixtures to seed data or interact with Python utilities
    cy.fixture('test-data').then((data) => {
      cy.request('POST', '/seed', data);
    });
  });

  it('should load the homepage', () => {
    cy.visit('/');
    cy.contains('Welcome to the app');
  });

  it('should perform an action', () => {
    cy.get('[data-cy=button]').click();
    cy.url().should('include', '/dashboard');
  });
});
