import React from 'react';
import styled from 'styled-components';
import { Header, Container } from 'semantic-ui-react';
import theme from './theme';

const StyledHeader = styled(Header)`
  font-size: 3.8rem;
  text-align: center;
`;

const Lead = styled.p`
  font-family: ${theme.hangeulNuri};
  text-align: center;
  font-size: 1.4rem;
  font-weight: 300;
  font-color: ${theme.gray3};
  margin-top: 1.5rem;
`;

const Heading = () => {
  return (
    <Container 
      style={{ 
        marginTop: '3em', 
        marginBottom: '6em', 
      }}
    >
      <StyledHeader
        as='h1' 
        textAlign='center'
      >
        👩🏼‍🍳 Variable Chef 👨🏼‍🍳
      </StyledHeader>
      <Lead>변수명을 요리해드립니다</Lead>
    </Container>
  );
};

export default Heading;