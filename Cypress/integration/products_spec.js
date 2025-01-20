describe('Palace of Goods - Products', () => {
  beforeEach(() => {
    cy.visit('/products');
  });

  it('should display a list of products', () => {
    cy.get('.product-card').should('have.length.greaterThan', 0);
  });

  it('should navigate to the product details page when a product is clicked', () => {
    cy.get('.product-card').first().click();
    cy.url().should('include', '/product/');
    cy.get('.product-title').should('exist');
  });
});
