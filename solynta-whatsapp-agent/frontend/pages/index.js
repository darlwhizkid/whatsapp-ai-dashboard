import React from 'react';

export default function Dashboard() {
  return (
    <div className="dashboard">
      <h1>WhatsApp AI Agent Dashboard</h1>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Active Chats</h3>
          <div className="stat-value">23</div>
        </div>
        <div className="stat-card">
          <h3>Messages Today</h3>
          <div className="stat-value">145</div>
        </div>
      </div>
      <div className="chat-monitor">
        {/* Real-time chat monitoring */}
      </div>
    </div>
  );
}
