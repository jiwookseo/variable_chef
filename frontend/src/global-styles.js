import { createGlobalStyle } from 'styled-components';
import theme from './theme';

export const GlobalStyle = createGlobalStyle`
  @font-face { 
    font-family: 'HangeulNuri-Bold'; 
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_three@1.0/HangeulNuri-Bold.woff') format('woff'); 
    font-weight: normal; 
    font-style: normal;
  }

  body {
    font-family: 'Muli', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;

  h1 {
    font-family: ${theme.breeSerif};
    font-size: 3rem;
    font-color: ${theme.gray3};
  }
`;