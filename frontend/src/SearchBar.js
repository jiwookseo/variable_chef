import React, { Fragment } from 'react';
import { Button, Select, Input } from 'semantic-ui-react';
// import styled from 'styled-components';
// import theme from './theme';

const options = [
  { key: '1', text: 'Python', value: 'python' },
  { key: '2', text: 'JavaScript', value: 'javascript' },
]

const SearchBar = (props) => {
  const {
    value,
    onChange,
    onSubmit
  } = this.props;

  return (
    <Fragment 
      style={{ marginBottom: '3em' }}
    >
      <Input 
        type='text' 
        placeholder='한글 단어' 
        action
      >
        <Select 
          compact 
          options={options} 
          defaultValue='python'
        />
        <input />
        <Button 
          type='submit' 
          inverted 
          color='green'
        >
          Cook
        </Button>
      </Input>

      <p>{value}</p>
    </Fragment>
  );
};

export default SearchBar;