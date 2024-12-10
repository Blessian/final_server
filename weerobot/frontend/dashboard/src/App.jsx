import React from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import CCTVSection from './components/CCTVSection';
import DataSection from './components/DataSection';
import VideoModal from './components/VideoModal';

// 테마 설정
const theme = createTheme({
  palette: {
    primary: {
      main: '#4dd0e1',
    },
    background: {
      default: '#e0f7fa',
    },
  },
});

// QueryClient 설정
const queryClient = new QueryClient();

function App() {
  console.log('App component rendered'); // 디버깅용 로그

  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Box sx={{ display: 'flex', height: '100vh', p: 2 }}>
          <CCTVSection />
          <DataSection />
          <VideoModal />
        </Box>
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;