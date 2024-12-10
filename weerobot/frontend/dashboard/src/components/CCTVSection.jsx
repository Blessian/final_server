import { Box, Paper, Typography } from '@mui/material';
import { useSocket } from '../hooks/useSocket';

function CCTVSection() {
  useSocket(); // 소켓 연결 설정

  return (
    <Box sx={{ flex: 1, p: 2 }}>
      <Paper
        elevation={3}
        sx={{
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          p: 2,
        }}
      >
        <Typography variant="h5" gutterBottom>
          CCTV Monitoring
        </Typography>
        <Box
          sx={{
            flex: 1,
            bgcolor: 'black',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <Typography color="white">
            Waiting for CCTV stream...
          </Typography>
        </Box>
      </Paper>
    </Box>
  );
}

export default CCTVSection;