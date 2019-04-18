import React, { Fragment } from 'react';
import { Header, Popup } from 'semantic-ui-react';
import styled from 'styled-components';

const Like = styled.span`

`;

const WordItem = (props) => {
  const { name, like } = props;
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'space-between',
    }}>
      <Header as='h3' style={{ display: 'inline' }}>{name}</Header>
      <Like>{like}</Like>
    </div>
  );
};

const CopyPopup = () => (
  <Popup trigger={<WordItem />} content='Click to copy' inverted />
)

export default WordItem;