import React, { Fragment } from 'react';
import { Segment, Header, Popup, Button } from 'semantic-ui-react';
import styled from 'styled-components';

const Like = styled.span`

`;

const Variable = styled.span`

`

const WordItem = (props) => {
  const { name, like } = props;
  return (
    <Segment
      style={{
        display: 'flex',
        justifyContent: 'space-between',
      }}
    >
      <Variable>{name}</Variable>
      <Like>{like}</Like>
    </Segment>
  );
};

const CopyPopup = () => (
  <Popup trigger={<WordItem />} content='Click to copy' inverted />
)

export default WordItem;