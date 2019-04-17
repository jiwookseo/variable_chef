import React from 'react';
import { Header, Container } from 'semantic-ui-react';

const Heading = () => {
  return (
    <Container style={{ marginTop: '3em' }}>
      <Header as='h1' textAlign='center'>Variable Chef</Header>
    </Container>
  );
};

export default Heading;