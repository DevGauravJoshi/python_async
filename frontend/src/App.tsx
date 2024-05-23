import React from "react";
import UserLogin from "./components/UserLogin";
import ChatPage from "./components/ChatPage";

import AuthProvider from "./context/AuthContext";
import { ProtectedRoutes } from "./secure_routes/ProtectedRoutes";

import { Navigate, Route, Routes } from "react-router-dom";

const App: React.FC = () => {
  return (
    <div>
      <AuthProvider>
        <Routes>
          <Route path="*" element={<Navigate to="/" replace />} />
          <Route path="/" element={<UserLogin />} />
          <Route
            path="/chat/:roomname"
            element={
              <ProtectedRoutes>
                <ChatPage />
              </ProtectedRoutes>
            }
          />
        </Routes>
      </AuthProvider>
    </div>
  );
};

export default App;
