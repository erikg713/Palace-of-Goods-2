describe('Palace of Goods - Homepage', () => {
  it('should load the homepage and display the correct title', () => {
    cy.visit('/');
    cy.title().should('include', 'Palace of Goods');
    cy.get('header').should('be.visible').and('contain', 'Welcome to Palace of Goods');
  });
});
