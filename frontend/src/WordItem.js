import React, { Component } from 'react';
import { Segment, Header, Popup, Button } from 'semantic-ui-react';
import styled from 'styled-components';

const Like = styled.span`

`;

const Variable = styled.span`

`

class WordItem extends Component {
  constructor(props) {
    super(props);
    this.state = {
      like: 0
    }
  }
  render() {
    return (
      <Segment
        key={this.props.key}
        style={{
          display: 'flex',
          justifyContent: 'space-between',
        }}
      >
        <Variable>{this.props.name}</Variable>
        <Like>{this.state.like}</Like>
      </Segment>
    );
  }
};

const CopyPopup = () => (
  <Popup trigger={<WordItem />} content='Click to copy' inverted />
)

export default WordItem;