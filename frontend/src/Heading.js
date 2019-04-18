import React from 'react';
import styled from 'styled-components';
import { Header, Container } from 'semantic-ui-react';

const StyledHeader = styled(Header)`
  font-size: 3.5rem;
  text-align: center;
`;

const Lead = styled.p`
  text-align: center;
  font-size: 1.2rem;
  font-weight: 300;
`;

const Heading = () => {
  return (
    <Container 
      style={{ 
        marginTop: '3em', 
        marginBottom: '4em', 
      }}
    >
      <StyledHeader
        as='h1' 
        textAlign='center'
      >
        👩🏻‍🍳 Variable Chef 👨🏻‍🍳
      </StyledHeader>
      <Lead>변수명을 요리해드립니다</Lead>
    </Container>
  );
};

export default Heading;