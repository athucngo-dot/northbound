let logoutHandler: null | (() => void) = null;

// A simple event system for auth-related events like logout
export const authEvents = {
    setLogoutHandler(fn: () => void) {
        logoutHandler = fn;
    },

    triggerLogout() {
        logoutHandler?.();
    }
};