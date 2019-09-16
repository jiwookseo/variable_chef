import React, { Fragment } from 'react';
import PropTypes from 'prop-types';
import { Form, Label, Select } from 'semantic-ui-react';
// import styled from 'styled-components';
// import theme from './theme';

const languages = [
  { key: 'python', text: 'Python', value: 'python' },
  { key: 'javascript', text: 'JavaScript', value: 'javascript' },
  { key: 'java', text: 'Java', value: 'java' },
  { key: 'c', text: 'C', value: 'c' },
  { key: 'cpp', text: 'C++', value: 'cpp' },
];

const SearchBar = (props) => {
  const { 
    word, 
    lang,
    wordError,
    onChange,
    onSubmit,
  } = props;

  const Options = languages.map(lang => 
    <option key={lang.key} value={lang.value}>{lang.text}</option>
  );

  return (
    <Form 
      onSubmit={onSubmit}
      style={{ marginBottom: '3em' }}
    >
      <Form.Group>
        <Form.Field>
          <select 
            name='lang'
            value={lang} 
            onChange={onChange}
            placeholder='사용 언어'
          >
            {Options}
          </select>
        </Form.Field>
        <Form.Field>
          <Form.Input
            placeholder='한글 단어'
            onChange={onChange}
            name='word'
            value={word}
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