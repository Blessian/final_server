import { QueryClient, QueryClientProvider } from 'react-query';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import CCTVSection from './components/CCTVSection';
import DataSection from './components/DataSection';
import VideoModal from './components/VideoModal';

const theme = createTheme({
  palette: {
    primary: {
      main: '#4dd0e1', // mint green
    },
    background: {
      default: '#e0f7fa',
    },
  },
});

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Box sx={{ display: 'flex', height: '100vh' }}>
          <CCTVSection />
          <DataSection />
          <VideoModal />
        </Box>
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;