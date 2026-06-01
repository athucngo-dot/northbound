import { useEffect, useState, useCallback } from "react";
import { AuthContext } from "../../features/auth/authContext";
import { usersApi } from "../../features/users/api";
import { authApi } from "../../features/auth/api";
import { authEvents } from "../../stores/authEvents";
import type { User } from "../../types/user";

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
    const [user, setUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);

    const fetchUser = useCallback(async () => {
        try {
            const user = await usersApi.me();
            setUser(user);
        } catch (err: any) {
            if (err.response?.status === 401) {
                setUser(null);
            } else {
                console.error("Unexpected error fetching user:", err);
            }
        } finally {
            setLoading(false);
        }
    }, []);

    useEffect(() => {
        fetchUser();
    }, [fetchUser]); // fetch user on mount

    const logout = useCallback(async () => {
        try {
            await authApi.logout();
        } finally {
            setUser(null);
        }
    }, []);

    useEffect(() => {
        authEvents.setLogoutHandler(logout);
    }, [logout]);

    const refreshUser = useCallback(async () => {
        setLoading(true);
        await fetchUser();
    }, [fetchUser]);


    return (
        <AuthContext.Provider
            value={{ user, loading, refreshUser, logout }}
        >
            {children}
        </AuthContext.Provider>
    );
};