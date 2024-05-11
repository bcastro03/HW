class Server {
    public static int minMeetingRooms(int[][] intervals) {
        int n = 1000010;
        int[] startEnd = new int[n];
        for (int[] e : intervals) {
            ++startEnd[e[0]];
            --startEnd[e[1]];
        }
        int res = startEnd[0];
        for (int i = 1; i < n; ++i) {
            startEnd[i] += startEnd[i - 1];
            res = Math.max(res, startEnd[i]);
        }
        return res;
    }

    public static void main(String[] args) {
        int[][] intervals = {{0, 2}, {1, 2}, {2, 3}};
        System.out.print(minMeetingRooms(intervals));
    }
}