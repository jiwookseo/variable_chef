import React, { Fragment } from 'react';
import PropTypes from 'prop-types';
import { Form, Label } from 'semantic-ui-react';
// import styled from 'styled-components';
// import theme from './theme';

const options = [
  { key: 'python', text: 'Python', value: 'python' },
  { key: 'javascript', text: 'JavaScript', value: 'javascript' },
  { key: 'java', text: 'Java', value: 'java' },
  { key: 'c', text: 'C', value: 'c' },
  { key: 'cpp', text: 'C++', value: 'cpp' },
]

const SearchBar = (props) => {
  const { 
    word, 
    lang,
    wordError,
    onChange,
    onSelect,
    onSubmit,
  } = props;

  // static propTypes = {
  //   word: PropTypes.string.isRequired,
  //   lang: PropTypes.string.isRequired,
  // };

  // static defaultProps = {
  //   word: '',
  //   lang: '',
  // };

  return (
    <Form 
      onSubmit={onSubmit}
      style={{ marginBottom: '3em' }}
    >
      <Form.Group>
        <Form.Select
          options={options} 
          name='lang'
          placeholder='사용 언어'
          onChange={onSelect}
          defaultValue={lang}
          style={{
            
          }}
        />
        <Form.Field>
          <Form.Input
            placeholder='한글 단어'
            name='word'
            onChange={onChange}
            defaultValue={word}
            error={wordError}
          />
          { wordError &&          
            <Label basic color='red' pointing>
              한글 단어를 입력해주세요.
            </Label>
          }
        </Form.Field>
        <Form.Button 
          content='Cook 🍳' 
          inverted color='green'
          type='submit'
          disabled={
            !word || !lang
          }
        />
      </Form.Group>
    </Form>
  );
};

export default SearchBar;