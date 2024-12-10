import React from 'react';
import { Box, Paper, Typography, Divider } from '@mui/material';
import RobotList from './Lists/RobotList';
import CCTVList from './Lists/CCTVList';
import CCTVLogList from './Lists/CCTVLogList';
import RobotLogList from './Lists/RobotLogList';
import ChatList from './Lists/ChatList';

function DataSection() {
  return (
    <Box sx={{ flex: 1 }}>
      <Paper elevation={3} sx={{ height: '100%', p: 2, overflow: 'auto' }}>
        {/* Robots Section */}
        <Typography variant="h6" gutterBottom sx={{ color: '#4dd0e1' }}>
          Robots
        </Typography>
        <RobotList />
        <Divider sx={{ my: 2 }} />

        {/* CCTVs Section */}
        <Typography variant="h6" gutterBottom sx={{ color: '#4dd0e1' }}>
          CCTVs
        </Typography>
        <CCTVList />
        <Divider sx={{ my: 2 }} />

        {/* CCTV Logs Section */}
        <Typography variant="h6" gutterBottom sx={{ color: '#4dd0e1' }}>
          CCTV Logs
        </Typography>
        <CCTVLogList />
        <Divider sx={{ my: 2 }} />

        {/* Robot Logs Section */}
        <Typography variant="h6" gutterBottom sx={{ color: '#4dd0e1' }}>
          Robot Logs
        </Typography>
        <RobotLogList />
        <Divider sx={{ my: 2 }} />

        {/* Chat Section */}
        <Typography variant="h6" gutterBottom sx={{ color: '#4dd0e1' }}>
          Chat
        </Typography>
        <ChatList />
      </Paper>
    </Box>
  );
}

export default DataSection;