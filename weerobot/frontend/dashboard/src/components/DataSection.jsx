import React from 'react';
import { Box, Paper, Typography, Divider } from '@mui/material';
import RobotList from './Lists/RobotList';
import CCTVList from './Lists/CCTVList';
import CCTVLogList from './Lists/CCTVLogList';
import RobotLogList from './Lists/RobotLogList';
import ChatList from './Lists/ChatList';

function DataSection() {
  const listStyle = {
    maxHeight: '200px',  // 리스트 최대 높이 제한
    overflow: 'auto',    // 스크롤 가능하도록
    '& .MuiList-root': {
      padding: 0,        // 리스트 패딩 제거
    },
    '& .MuiListItem-root': {
      minHeight: '40px', // 각 항목의 최소 높이
      py: 0.5,          // 위아래 패딩 축소
    }
  };

  return (
    <Box sx={{ flex: 1 }}>
      <Paper elevation={3} sx={{ 
        height: '100%', 
        p: 2, 
        display: 'flex',
        flexDirection: 'column',
        gap: 2,
        overflow: 'hidden' // 전체 스크롤 방지
      }}>
        {/* Robots Section */}
        <Box>
          <Typography variant="h6" gutterBottom sx={{ color: '#4dd0e1' }}>
            Robots
          </Typography>
          <Box sx={listStyle}>
            <RobotList />
          </Box>
        </Box>

        {/* CCTVs Section */}
        <Box>
          <Typography variant="h6" gutterBottom sx={{ color: '#4dd0e1' }}>
            CCTVs
          </Typography>
          <Box sx={listStyle}>
            <CCTVList />
          </Box>
        </Box>

        {/* CCTV Logs Section */}
        <Box>
          <Typography variant="h6" gutterBottom sx={{ color: '#4dd0e1' }}>
            CCTV Logs
          </Typography>
          <Box sx={listStyle}>
            <CCTVLogList />
          </Box>
        </Box>

        {/* Robot Logs Section */}
        <Box>
          <Typography variant="h6" gutterBottom sx={{ color: '#4dd0e1' }}>
            Robot Logs
          </Typography>
          <Box sx={listStyle}>
            <RobotLogList />
          </Box>
        </Box>

        {/* Chat Section */}
        <Box>
          <Typography variant="h6" gutterBottom sx={{ color: '#4dd0e1' }}>
            Chat
          </Typography>
          <Box sx={listStyle}>
            <ChatList />
          </Box>
        </Box>
      </Paper>
    </Box>
  );
}

export default DataSection;